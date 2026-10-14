# name: Build and push
        id: build-and-push
        uses: docker/build-push-action@v6
        with:
          context: .
          file: images/Dockerfile
          tags: ${{ steps.meta.outputs.tags }}
          labels: ${{ steps.meta.outputs.labels }}
          build-args: |
            RUNNER_VERSION=${{ env.RUNNER_VERSION }}
            RUNNER_CONTAINER_HOOKS_VERSION=${{ env.RUNNER_CONTAINER_HOOKS_VERSION }}
          load: true
          push:
            ${{ github.event_name == 'push' && github.ref == 'refs/heads/main'
            && github.repository == 'usatlas/runner' }}

      - name: Generate attestation
        # every PR will trigger a push event on main, so check the push event is actually coming from main
        if:
          github.event_name == 'push' && github.ref == 'refs/heads/main' &&
          github.repository == 'usatlas/runner'
        uses: actions/attest-build-provenance@v3
        with:
          subject-name: ${{ env.REGISTRY }}/${{ env.IMAGE_NAME }}
          subject-digest: ${{ steps.build-and-push.outputs.digest }}
          push-to-registry: true
