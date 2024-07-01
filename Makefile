gen: clean
	curl -s https://developer.koyeb.com/public.swagger.json -o swagger.json
	docker run --rm -ti \
		-v ./sdk:/sdk \
		-w /sdk \
		-v ./swagger.json:/swagger.json:ro \
		openapitools/openapi-generator-cli \
			generate \
			-g python \
			-i /swagger.json

clean:
	rm -rf ./swagger.json ./sdk