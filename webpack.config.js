var path = require('path');

 module.exports = {
  context: __dirname + "/react",
  entry: './index.js',

  output: {
        filename: "bundle.js",
        path: __dirname+'/static/bundles/',
  },

  module: {
    rules: [
		{
		    test: /\.(js|jsx)$/,
		    loader: 'babel-loader',
		    exclude: /node_modules/,
   	query: {
           presets: ["es2015", "react"]
        }
		},

      { test: /\.css$/, loader: 'style-loader!css-loader' },
/**
      {
        test: /\.(png|gif|jpg)$/,
        include: [
          path.join(__dirname, '')
        ],
        loader: 'file-loader',
      }

  ***/
    ]
  },

  resolve: {
    extensions: ['.js', '.jsx', '.css']
  }

};