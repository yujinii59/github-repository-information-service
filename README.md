# GitHub Repository information Service

---

It is a service that get information about 
- repository name
- description
- number of open issues
- the title of the latest five issues

If you put the ``repository names`` what you want, you can get above data formatted json.

You can access the service using ``curl`` command or writing url on the web browser

```bash
curl http://127.0.0.1:5000/<repository-names>
```

---

## 1.  Obtain GitHub personal access token

If you have token, you can use it.

- Obtain the token that gave you the desired permissions
    
    [https://github.com/settings/tokens](https://github.com/settings/tokens)
    

## 2. Create environment variable or Create environment file

- environment variable
    
    ```bash
    export github_token=<your-access-token>
    ```
    
- environment file (`.env`)
    
    ```
    github_token = "<your-access-token>"
    ```
    

## 3. Run the Flask web framework running ``app.py``
```bash
python ./app.py
```