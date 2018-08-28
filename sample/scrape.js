bodyHTML = await page.evaluate(() => document.body.innerHTML);
await console.log(bodyHTML);

