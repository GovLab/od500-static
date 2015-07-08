'''
Generate a separate company page for every single company that completed a
survey, based off of JSON data.
'''

from pelican import signals
from pelican.generators import CachingGenerator
from pelican.contents import Page

from slugify import slugify


class Company(Page):
    '''
    Page subclass for companies.
    '''
    mandatory_properties = ('title', 'company',)
    default_template = 'company'


class CompaniesGenerator(CachingGenerator):
    """
    Generate companies pages.
    """

    def __init__(self, *args, **kwargs):
        self.companies = []
        super(CompaniesGenerator, self).__init__(*args, **kwargs)

    def generate_context(self):
        '''
        Generate company context.
        '''
        paths = set()  # set used to prevent country/slug dupes from bad data
        for _, country in self.settings['COUNTRIES'].iteritems():
            for company in country['companies']:
                country = company['country']
                slug = slugify(company['prettyName'])

                path = '{}/company/{}'.format(country, slug)
                # Prevent duplicate slugs
                if path in paths:
                    continue
                paths.add(path)

                company = self.get_cached_data(path, None)
                if company is None:
                    metadata = {
                        'country': country,
                        'slug': slug,
                        'company': company
                    }
                    company = Company(content='', metadata=metadata, settings=self.settings)
                    self.cache_data(path, company)

                    # is this right, or should it be one level above?
                    self.companies.append(company)

                self.add_source_path(company)

        self._update_context(('companies',))
        self.save_cache()
        self.readers.save_cache()


    def _get_file_stamp(self, filename):
        '''
        Override file stamp function to just look at companies.csv
        '''
        return self._filestamp_func('content/data/company.json')


    def generate_output(self, writer):
        '''
        Generate company output.
        '''
        for company in self.companies:
            self.context['company'] = company.metadata['company']
            writer.write_file(
                company.save_as, self.get_template(company.template),
                self.context, page=company,
                relative_urls=self.settings['RELATIVE_URLS'],
                override_output=hasattr(company, 'override_save_as'))


def generate_company_pages(sender): #pylint: disable=unused-argument
    '''
    Add the CompaniesGenerator.
    '''
    return CompaniesGenerator


def register():
    '''
    Register `generate_company_pages` with Pelican.
    '''
    signals.get_generators.connect(generate_company_pages)
