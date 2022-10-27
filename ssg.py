import typer
from ssg.site import Site


def main(source="content", dest="dist"):
    config = {
        "source": source,
        "dest": dest
    }
    x = Site(config["source"], config["dest"])
    x.build()


typer.run(main)
