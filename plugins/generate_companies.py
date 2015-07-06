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
        companies = self.settings['COMPANIES']

        prevent_dupes = set()  # set used to prevent country/slug dupes from bad data
        for company in companies:
            country = company['country']
            slug = slugify(company['prettyName'])

            # Prevent duplicate slugs
            if (country, slug,) in prevent_dupes:
                continue
            prevent_dupes.add((country, slug,))

            metadata = {
                'country': country,
                'slug': slug,
                'company': company
            }
            self.companies.append(
                Company(content='', metadata=metadata, settings=self.settings))


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
