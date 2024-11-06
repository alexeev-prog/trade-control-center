#!/usr/bin/python3
import sys
from app import create_app


def main():
	app = create_app()

	if len(sys.argv) > 1:
		if sys.argv[1] == 'db':
			with app[0].app_context():
				app[1].create_all()

	app[0].run(host='0.0.0.0', port=5000)


if __name__ == '__main__':
	main()

