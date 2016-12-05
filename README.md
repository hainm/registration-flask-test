1. Create a server

```bash
cd server
python app.py
```

2. Try build and install dummy package and send user info to database.db

```bash
cd client
conda build recipe
conda install /path/to/the/new/package
```

3. Check info. Open
`http://localhost:8000/list`
