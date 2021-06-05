# App settings

This sample shows a way to stoare app settings in *env vars* (as suggested in [twelve-factor]) using pydantic ``BaseSettings``

## Rationale: 

A [twelve-factor] app [stores config in environment variables](https://12factor.net/config) (often shortened to *env vars* or *env*)

- app config defined as [pydantic] ``BaseSettings`` constructed exclusively via envs and secrets. 
    - NOTE that ``BaseSettings`` has other construction mechanisms but we will intentionally avoid using them
    - 
- fields are *const* after construction (i.e. frozen or faux-immutable in python jargon)
- field names are capitalized to resemble the env names found in the ``.env`` file listings
- can print an .env list via the CLI



## References

 - The [twelve-factor] app
 - https://github.com/pcrespov/sandbox-python/tree/master/compose-settings


 [twelve-factor]:https://12factor.net
 [pydantic]:https://pydantic-docs.helpmanual.io/