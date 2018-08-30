// const projectName = xxx

/*
 * --------------------
 * Custom Args
 * --------------------
 */
var argv = require('argv');

/*
 * Usage: options['foo']
 */

// argv.option({
//  name: 'foo',
//  short: 'f',
//  type : 'string',
//  description :'This is a variable for test',
//  example: "'script --foo=1' or 'script -f 1'"
// });

options = argv.run()['options']

/*
 * ---------------------
 * Template Prefix
 * ---------------------
 */

var index = 0
const screenShotPath = () => {
  number = ("0" + index).slice(-2);
  index++;
  return './sel2pup/screenshot/' + projectName + '_' + number + '.png';
}

require('dotenv').config();
const env = process.env // env.XXX_XXX

const puppeteer = require("puppeteer");
puppeteer.launch().then(async browser => {
  pages = await browser.pages();
  page = await pages[0]
  try {

/*
 * ---------------------
 * Created by Script
 * ---------------------
 */

