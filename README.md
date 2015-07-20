# Home for new static OD500 site

### Building

You'll need to install the requirements in a virtualenv, and pull down the
`pelican-plugins` submodule.

    pip install -r requirements.txt
    git submodule init
    git submodule update
    npm install

Then you can build into `content`:

    ./build.sh

This will continuously monitor changes and rebuild when necessary. Ctrl-C to
stop.

You'll need to run a server to preview the content:

    ./serve.sh
