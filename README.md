# App settings

This sample shows a way to stoare app settings in *env vars* (as suggested in [twelve-factor]) using pydantic ``BaseSettings``



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

```commandline
$ python app settings --verbose 
APP_HOST=localhost
APP_PORT=80

# --- APP_POSTGRES --- 
POSTGRES_HOST=localhost
POSTGRES_PORT=5432
POSTGRES_USER=foo
POSTGRES_PASSWORD=**********
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

```commandline
$ python app settings --verbose --compact
APP_HOST=localhost
APP_PORT=80
APP_POSTGRES={"POSTGRES_HOST": "localhost", "POSTGRES_PORT": 5432, "POSTGRES_USER": "foo", "POSTGRES_PASSWORD": "**********", "POSTGRES_DB": "foodb", "POSTGRES_MINSIZE": 1, "POSTGRES_MAXSIZE": 50}
# Some Module Example
APP_MODULE_1={"MYMODULE_VALUE": 10}
APP_MODULE_2={"MYMODULE2_SOME_OTHER_VALUE": 33}
```

```commandline
python app settings --as-json          
{
  "APP_HOST": "localhost",
  "APP_PORT": 80,
  "APP_POSTGRES": {
    "POSTGRES_HOST": "localhost",
    "POSTGRES_PORT": 5432,
    "POSTGRES_USER": "foo",
    "POSTGRES_PASSWORD": "**********",
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

## Rationale: 

A [twelve-factor] app [stores config in environment variables](https://12factor.net/config) (often shortened to *env vars* or *env*)

- app config defined as [pydantic] ``BaseSettings`` constructed exclusively via envs and secrets. 
    - NOTE that ``BaseSettings`` has other construction mechanisms but we will intentionally avoid using them
    - 
- fields are *const* after construction (i.e. frozen or faux-immutable in python jargon)
- field names are capitalized to resemble the env names found in the ``.env`` file listings
- can print an .env list via the CLI


## Features

- A [typer] CLI
- 

## References

 - The [twelve-factor] app
 - https://github.com/pcrespov/sandbox-python/tree/master/compose-settings


 [twelve-factor]:https://12factor.net
 [pydantic]:https://pydantic-docs.helpmanual.io/
 [typer]:https://typer.tiangolo.com/