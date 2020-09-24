from invoke import Responder


class WatchersFactory:
    @staticmethod
    def create_watchers(watchers_config):
        watchers = []
        for watcher_conf in watchers_config:
            watchers.append(
                Responder(
                    pattern=r"{}".format(watcher_conf["pattern"]),
                    response=watcher_conf["response"],
                )
            )

        return watchers
