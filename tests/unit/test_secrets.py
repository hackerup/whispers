import pytest

from whispers import core

from .conftest import FIXTURE_PATH, config_path, fixture_path


@pytest.mark.parametrize("configfile", ["exclude_keys.yml", "exclude_values.yml"])
@pytest.mark.parametrize("src", ["excluded.yml", "excluded.json", "excluded.xml"])
def test_exclude_by_keys_and_values(configfile, src):
    config = core.load_config(config_path(configfile), FIXTURE_PATH)
    secrets = core.run(fixture_path(src), config=config)
    assert next(secrets).key == "hardcoded_password"
    with pytest.raises(StopIteration):
        next(secrets)


@pytest.mark.parametrize(
    ("src", "keys"),
    [
        ("privatekeys.yml", ["access", "key", "rsa", "dsa", "ec", "openssh"]),
        ("privatekeys.json", ["access", "key", "rsa", "dsa", "ec", "openssh"]),
        ("privatekeys.xml", ["access", "key", "rsa", "dsa", "ec", "openssh"]),
        ("aws.yml", ["aws_id", "aws_key", "aws_token"]),
        ("aws.json", ["aws_id", "aws_key", "aws_token"]),
        ("aws.xml", ["aws_id", "aws_key", "aws_token"]),
        ("jenkins.xml", ["noncompliantApiToken", "noncompliantPasswordHash"]),
        ("cloudformation.yml", ["NoncompliantDBPassword"]),
        ("cloudformation.json", ["NoncompliantDBPassword"]),
    ],
)
def test_detection_by_key(src, keys):
    secrets = core.run(fixture_path(src))
    for key in keys:
        assert next(secrets).key == key
    with pytest.raises(StopIteration):
        next(secrets)


@pytest.mark.parametrize(
    ("src", "count"),
    [
        ("custom.yml", 0),
        ("custom.json", 0),
        ("custom.xml", 0),
        ("hardcoded.yml", 5),
        ("hardcoded.json", 5),
        ("hardcoded.xml", 5),
        ("passwords.yml", 4),
        ("passwords.json", 4),
        ("passwords.xml", 4),
        ("placeholders.yml", 0),
        ("placeholders.json", 0),
        ("placeholders.xml", 0),
        ("apikeys.yml", 10),
        ("apikeys.json", 10),
        ("apikeys.xml", 10),
        (".npmrc", 3),
        (".pypirc", 1),
        ("pip.conf", 2),
        ("integration.conf", 5),
        ("integration.yml", 5),
        ("integration.json", 5),
        ("integration.xml", 5),
        ("settings.conf", 1),
        ("settings.cfg", 1),
        ("settings.ini", 1),
        ("settings.env", 1),
        ("shell.sh", 13),
        ("Dockerfile", 3),
        ("beans.xml", 3),
        ("jdbc.xml", 3),
        (".htpasswd", 2),
        (".aws/credentials", 3),
        ("falsepositive.yml", 4),
        ("source.py", 5),
        ("plaintext.txt", 2),
        ("uri.yml", 2),
    ],
)
def test_detection_by_value(src, count):
    secrets = core.run(fixture_path(src))
    for _ in range(count):
        value = next(secrets).value.lower()
        if value.isnumeric():
            value = bytes.fromhex(hex(int(value))[2:]).decode("ascii")
        assert "hardcoded" in value
    with pytest.raises(StopIteration):
        next(secrets)
