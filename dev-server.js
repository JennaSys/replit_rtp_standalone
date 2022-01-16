const Bundler = require('parcel-bundler');
const express = require('express');


const app = express();

// parcel optionsdebug=True,
const options = {minify:false, cache: true, outDir: 'dist/dev', logLevel: 4};

const bundler = new Bundler('src/index.html', options);
app.use(bundler.middleware());

bundler.on('buildEnd', () => {
  console.log('Parcel proxy server has started');
});

app.listen(3000);
