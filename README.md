# Snowflake Connector Lite

# Overview

This repository contains a lite version of snowflake connector python package

# Why?

Because the current snowflake python package dependencies are too restrictive for automated deployments. A simple look at the [package](https://github.com/snowflakedb/snowflake-connector-python) shows that Snowflake's current package has grown due to the needs to support legacy customers with unique needs.

Currently, installing snowflake-connector (or snowflake-sqlalchemy) on a new machine or any automatic deployment has a chance of failling due to snowflake-connector's requirements.

This package aims to reduce the dependencies. You get a connection, thats all


## Usage


###  Installation

```sh
$ pip install snowflake-connector-lite
```

### Import

Usage of snowflake-connector-lite mirrors the official snowflake-connector-python package, **except** it does not support the most advanced features of that package (like cloud integrations)

```Python
from snowflake.connector import connect
con=connect(user='$SNOWFLAKE_USER',
            password='$SNOWFLAKE_PWD',
            account='$SNOWFLAKE_ACCOUNT',
            host='$SNOWFLAKE_ACCOUNT.snowflakecomputing.com')
con.cursor().execute('SELECT * FROM TABLE').fetchall())
```


## TODOs

This package is a WIP, feel free to submit a PR to reduce the dependencies even more!.
I would like to get rid of the hardcoding of requests version and avoid **monkeypatching urllib to use PyOpenSSL (actual implementation in the official package)**


License
----

This package has the same license as the original snowflake-connector-python package (Apache License Version 2.0, January 2004)
