docker build -f Dockerfile.bird-feeder -t bird-feeder .

docker build -f Dockerfile.albatross -t albatross . 

echo "=== albatross ==="
docker run -it --rm albatross python -c "from albatross import main; main.test()"
echo "\n"


echo "=== bird-feeder ==="
docker run -it --rm bird-feeder python -c "from bird_feeder import foo; foo.test()"
echo "\n"