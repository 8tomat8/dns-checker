import click
import pydig
from sys import stderr

# list parsed from the dns-checker.com
# can be outdated
nameservers = [
    "208.67.222.220",
    "204.117.214.10",
    "8.8.8.8",
    "8.26.56.26",
    "208.79.56.204",
    "195.46.39.39",
    "197.189.234.82",
    "89.104.166.243",
    "83.145.86.7",
    "84.236.142.130",
    "194.209.157.109",
    "37.235.1.174",
    "84.200.70.40",
    "200.56.224.11",
    "177.43.76.244",
    "211.25.206.147",
    "1.1.1.1",
    "202.136.162.11",
    "168.126.63.1",
    "180.76.76.76",
    "31.7.37.37",
    "103.193.252.2",
    "111.68.99.194",
    "185.228.168.9"
]

@click.command()
@click.option('-t', '--type', 'record_type', default='A', type=str)
@click.argument('domain', required=True, type=str)
def main(record_type, domain):
    errors = []
    for ns in nameservers:
        resolver = pydig.Resolver(
            nameservers = [ns]
        )

        resp = set(resolver.query(domain, record_type))
        if len(resp) == 0:
            errors.append(f"Response from the {ns} is empty")
            continue

        prevResp = resp

    for err in errors:
        print(err)

    if len(errors) == 0:
        print(f'All {len(nameservers)} nameservers responded!')

if __name__ == "__main__":
    main()
