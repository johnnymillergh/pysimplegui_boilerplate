from pysimplegui_boilerplate.configuration.application_configuration import configure


def test_configure() -> None:
    try:
        configure()
    except Exception as ex:
        assert False, f"{configure} raised an exception {ex}"
