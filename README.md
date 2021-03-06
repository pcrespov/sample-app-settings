# App settings


- A [twelve-factor] app [stores config in environment variables](https://12factor.net/config) (often shortened to *env vars* or *env*)
- Every deployment uses a different configuration which is defined in a envfile or with secrets (see e.g. https://github.com/ITISFoundation/osparc-ops/tree/master/services/simcore)
- The variables in the configuration might change with different app versions (adds/removes/modifies)
  - Need an easy way to reproduce envfiles



## Requirements:

- app's configuration is stored in a [pydantic] ``Settings`` instance
  - ``Settings`` instance automatically captures *envs* and *secrets* upon construction
  - Note that any other construction mechanisms is intentionally avoided
- a sigle ``Settings`` per app initialized upon startup
    - each app submodule might define its own ``BaseSettings`` class but instances are added as sections in the app ``Settings`` and initialized at the same time
- fields are *const* after construction (i.e. frozen or faux-immutable in python jargon)
- field names are **capitalized** to simplify identifying the corresponding env name (multiple env captures must be really justified)
- CLI can print *envfiles* or json configurations


## Demo

This app assumes three modules:
  - **postgres** is a common module so the app uses the settings provided in ``settingslib``
  - **mod1** and **mod2** are two custom modules with arbitrary settings

Assuming that all required envs are in place (e.g. rename any of the ``.env-*`` samples  as ``.env``) we can display the
configuration resolved by the app:

```commandline
$ python app settings --as-json

{
  "APP_HOST": "localhost",
  "APP_PORT": 80,
  "APP_POSTGRES": {
    "POSTGRES_HOST": "localhost",
    "POSTGRES_PORT": 5432,
    "POSTGRES_USER": "foo",
    "POSTGRES_PASSWORD": "secret",
    "POSTGRES_DB": "foodb",
    "POSTGRES_MINSIZE": 1,
    "POSTGRES_MAXSIZE": 50
  },
  "APP_MODULE_1": {
    "MYMODULE_VALUE": 10
  },
  "APP_MODULE_2": {
    "MYMODULE2_SOME_OTHER_VALUE": 33
  }
}
```

Can actually get the json-schema as

```commandline
python app settings --as-json-schema

{
  "title": "Settings",
  "description": "The app settings",
  "type": "object",
  "properties": {
    "APP_HOST": {
      "title": "App Host",
...
```


The app captures the ``Settings`` from the *env vars* and it can be printed as an *envfile*

```commandline
$ python app settings --verbose

APP_HOST=localhost
APP_PORT=80

# --- APP_POSTGRES ---
POSTGRES_HOST=localhost
POSTGRES_PORT=5432
POSTGRES_USER=foo
POSTGRES_PASSWORD=secret
# Database name
POSTGRES_DB=foodb
# Maximum number of connections in the pool
POSTGRES_MINSIZE=1
# Minimum number of connections in the pool
POSTGRES_MAXSIZE=50

# --- APP_MODULE_1 ---
# Some value for module 1
MYMODULE_VALUE=10

# --- APP_MODULE_2 ---
MYMODULE2_SOME_OTHER_VALUE=33
```

or even more compact using json as values

```commandline
$ python app settings --verbose --compact

APP_HOST=localhost
APP_PORT=80
APP_POSTGRES={"POSTGRES_HOST": "localhost", "POSTGRES_PORT": 5432, "POSTGRES_USER": "foo", "POSTGRES_PASSWORD": "secret", "POSTGRES_DB": "foodb", "POSTGRES_MINSIZE": 1, "POSTGRES_MAXSIZE": 50}
# Some Module Example
APP_MODULE_1={"MYMODULE_VALUE": 10}
APP_MODULE_2={"MYMODULE2_SOME_OTHER_VALUE": 33}
```


## Usage

```commandline
$ python app settings --help
Usage: app settings [OPTIONS]

  Resolves settings and prints envfile

Options:
  --as-json / --no-as-json        [default: False]
  --as-json-schema / --no-as-json-schema
                                  [default: False]
  --compact / --no-compact        Print compact form  [default: False]
  --verbose / --no-verbose        [default: False]
  --help                          Show this message and exit.
```
## References

 - The [twelve-factor] app
 - [pydantic] settings
 - [typer] CLI
 - Original trials: https://github.com/pcrespov/sandbox-python/tree/master/compose-settings


 [twelve-factor]:https://12factor.net
 [pydantic]:https://pydantic-docs.helpmanual.io/
 [typer]:https://typer.tiangolo.com/