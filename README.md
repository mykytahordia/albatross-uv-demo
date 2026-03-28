# albatross-uv-demo

## Structure
```bash
albatross
├── packages/
│   └── bird-feeder/
│       ├── pyproject.toml   # <- subproject
│       └── src/
│           └── bird_feeder/
│               ├── __init__.py
│               └── foo.py
├── pyproject.toml            # <- root project
├── src/
│   └── albatross/
│       ├── __init__.py
│       └── main.py
├── Dockerfile.albatross
├── Dockerfile.bird-feeder
└── test.sh
```
## Dependencies

```toml
albatross:
    "bird-feeder"

    extra "np":
        "numpy"

bird-feeder:
    "albatross"
    "httpie"            
```

## Testing
To test the setup run:
```bash
chmod +x test.sh
./test.sh
```
Or manually
1. Build images
```bash
docker build -f Dockerfile.bird-feeder -t bird-feeder .
docker build -f Dockerfile.albatross -t albatross .
```

2. Run tests
```bash
docker run -it --rm albatross python -c "from albatross import main; main.test()"
docker run -it --rm bird-feeder python -c "from bird_feeder import foo; foo.test()"
```

Excpected output:
``` bash
=== albatross ===
httpie from bird-feeder is not present
core_fun
OK 2.4.3


=== bird-feeder ===
numpy from core module extra is not present
core_fun
OK 3.2.4
```