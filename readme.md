# sel2pup

The Converter From `xxx.side file recorded by Selenium IDE` to `xxx.js file with Puppeteer` in order to automate your operation at browser.

# Usage

1. Track your operation by SeleniumIDE
2. Export xxx.side file by SeleniumIDE
3. Execute command `python ./converters/parser.py -i xxx.side` to export `xxx.yml` file
4. Replace secret information in `xxx.yml` with `{DOTENV_NAME}`
5. Execute command `python ./converters/dotenv.py -i xxx.yml` to export `.env` file
6. Write down secret information in `.env` file -- it'll be not managed by Git
7. Execute command `python ./converters/generator.py -i xxx.yml` to export `xxx.js` file
8. Customize source code `xxx.js` as you like -- e.g. loop, using custom variables, getting DOM values
9. Execute command `node xxx.js` with Puppeteer
10. Execute command `find ./screenshot/*.png | xargs open` to check images

# Requirements

- Python
- Node.js

# Roadmap to v1.0.0

- [ ] divide modules tightly coupled into each parts
- [ ] add test code
- [ ] enable script to export images to cloud strage like S3 / GCS
- [ ] use CircleCI or TravisCI
- [ ] manage library dependencies as code
- [ ] define support version about Python & Node.js
- [ ] write usage document for programmer
- [ ] write usage document for non-programmer
- [ ] add open source license

