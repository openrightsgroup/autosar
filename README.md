# Making Subject Access Requests under the UK Data Protection Act 

## Quick Start

1. Set up the base environment

    ```
    git clone git@github.com:openrightsgroup/autosar.git
    cd autosar
    virtualenv ./
    ```
    
2. Enter the env

    ```
    source bin/activate
    ```
    
3. Install the dependencies

    ```
    pip install django
    pip install requests
    ```
    
4. Start the server

    ```
    python manage.py runserver
    ```

## Editing templates

1. Enter the folder `requests/templates`.
2. Edit the files in there.