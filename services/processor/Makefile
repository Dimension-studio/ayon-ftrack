include .env
VERSION := $(shell python3 -c "import os; import sys; content={}; exec(open('$(CURDIR)/../../package.py').read(), content); print(content['version'])")
BASE_NAME := ayon-dim-ftrack-processor
IMAGE := dimension-studio/$(BASE_NAME):$(VERSION)
BASH_CONTAINER_NAME := $(BASE_NAME)-bash-$(VERSION)

buildimage:
	cp -r ../../client/ayon_ftrack/common/ ./ftrack_common
	@echo $(VERSION)
	docker build -t dimension-studio/$(BASE_NAME):$(VERSION) .
	docker tag dimension-studio/$(BASE_NAME):$(VERSION) ghcr.io/dimension-studio/$(BASE_NAME):$(VERSION)
	docker push ghcr.io/dimension-studio/$(BASE_NAME):$(VERSION)
	rm -rf ftrack_common

clean:
	docker rmi $(image)

dev:
	cp -r ../../client/ayon_ftrack/common/ ./ftrack_common
	docker run --rm -ti \
		-v $(CURDIR):/service \
		--hostname dim-ftrackproc \
		--env AYON_API_KEY=${AYON_API_KEY} \
		--env AYON_SERVER_URL=${AYON_SERVER_URL} \
		--env AYON_ADDON_NAME=dim-ftrack \
		--env AYON_ADDON_VERSION=$(VERSION) \
		$(IMAGE) python -m processor
	rm -rf ftrack_common

bash:
	docker run --name $(BASH_CONTAINER_NAME) --rm -it --entrypoint /bin/bash $(IMAGE)