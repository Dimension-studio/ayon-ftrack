include .env
VERSION := $(shell python3 -c "import os; import sys; content={}; exec(open('$(CURDIR)/../../package.py').read(), content); print(content['version'])")
BASE_NAME := ayon-dim-ftrack-leecher
IMAGE := dimension-studio/$(BASE_NAME):$(VERSION)
BASH_CONTAINER_NAME := $(BASE_NAME)-bash-$(VERSION)

# Phony targets to prevent conflicts with file names
.PHONY: build clean

build:
	@echo $(VERSION)
	docker build -t dimension-studio/$(BASE_NAME):$(VERSION) .

clean:
	docker rmi $(IMAGE)

dev:
	docker run --rm -ti \
		-v $(CURDIR):/service \
		--env AYON_API_KEY=${AYON_API_KEY} \
		--env AYON_SERVER_URL=${AYON_SERVER_URL} \
		--env AYON_ADDON_NAME=ftrack \
		--env AYON_ADDON_VERSION=$(VERSION) \
		$(IMAGE) python -m leecher

bash:
	docker run --name $(BASH_CONTAINER_NAME) --rm -it --entrypoint /bin/bash $(IMAGE)

pushimage:
    docker build -t dimension-studio/$(BASE_NAME):$(VERSION) .
    docker tag $(BASE_NAME)$(VERSION) ghcr.io/dimension-studio/$(BASE_NAME):$(VERSION)
    docker push ghcr.io/dimension-studio/$(BASE_NAME):$(VERSION)