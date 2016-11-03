var webpack = require('webpack');
var HtmlWebpackPlugin = require('html-webpack-plugin');
var CopyWebpackPlugin = require('copy-webpack-plugin');
var CleanWebpackPlugin = require('clean-webpack-plugin');
var ExtractTextWebpackPlugin = require('extract-text-webpack-plugin');
var autoprefixer = require('autoprefixer');

var cssExtractor = new ExtractTextWebpackPlugin('styles/[name].css');
var lifecycleEvent = process.env.npm_lifecycle_event;


var devConfig = {
    entry: './src/app.jsx',
    output: {
        publicPath: '/',
        path: __dirname + '/public',
        filename: 'js/app.js'
    },
    devtool: 'source-map',
    module: {
        preLoaders: [
            // {
                // test: /\.jsx?$/,
                // loaders: ['eslint'],
                // exclude: /node_modules/
            // }
        ],
        loaders: [
            {
                test: /\.s?css$/,
                loaders: ['style', 'css', 'postcss', 'sass']
            },
            {
                test: /\.jsx?$/,
                exclude: /(node_modules|bower_components)/,
                loaders: ['babel-loader']
            },
            {
                test: /\.(eot|ttf|woff|woff2|otf)(\?\S*)?$/,
                loaders: ['file?name=fonts/[name].[ext]']
            },
            { 
                test: /\.(png|jpg|jpeg|gif|woff|svg)$/,
                exclude: /favicon/,
                loader: 'file-loader'
            }
        ]
    },
    postcss: [
        autoprefixer({ browsers: ['last 3 versions'] })
    ],
    plugins: [
        new HtmlWebpackPlugin({
            title: 'Webpack Build',
            template: './src/index.html'
        }),
        new webpack.DefinePlugin({
            'process.env.NODE_ENV': '"development"'
        })
    ],
    devServer: {
        historyApiFallback: true,
        contentBase: './public',
        proxy: {
            '/api': {
                target: 'http://localhost:9090',
                xfwd: true,
                changeOrigin: true
            }
        }
    }
}

var buildConfig = {
    entry: './src/app.jsx',
    output: {
        publicPath: '/',
        path: __dirname + '/public',
        filename: 'js/app.js'
    },
    devtool: 'source-map',
    module: {
        preLoaders: [
            // {
                // test: /\.jsx?$/,
                // loaders: ['eslint'],
                // exclude: /node_modules/
            // }
        ],
        loaders: [
            {
                test: /\.s?css$/,
                loader: cssExtractor.extract(['css', 'postcss', 'sass'])
            },
            {
                test: /\.jsx?$/,
                exclude: /(node_modules|bower_components)/,
                loaders: ['babel']
            },
            {
                test: /\.(eot|ttf|woff|woff2|otf)(\?\S*)?$/,
                loaders: ['file?name=fonts/[name].[ext]']
            },
            { test: /\.(png|jpg|jpeg|gif|woff|svg)$/, loader: 'file-loader' }
        ]
    },
    postcss: [
        autoprefixer({ browsers: ['last 3 versions'] })
    ],
    plugins: [
        new HtmlWebpackPlugin({
            title: 'Webpack Build',
            template: './src/index.html'
        }),
        new webpack.DefinePlugin({
            'process.env.NODE_ENV': '"production"'
        }),
        new CleanWebpackPlugin(['public/fonts', 'public/js', 'public/styles', 'public/index.html']),
        cssExtractor,
        new webpack.optimize.UglifyJsPlugin({
            compress: {
                warnings: false
            },
            sourceMap: true,
            minimize: true
        }),
        new CopyWebpackPlugin([
            {context: "./src/favicon/", from: '**/*', to: './favicon/'},
            {context: "./src/vendor/", from: '**/*', to: './vendor/'}
        ])
    ],
    devServer: {
        historyApiFallback: true,
        contentBase: './public',
        proxy: {
            // proxy to production api
            '/api': {
                target: 'http://localhost:9090',
                xfwd: true,
                changeOrigin: true
            }
        }
    }
}

switch (lifecycleEvent) {
    case 'build':
    module.exports = buildConfig;
    break;
    default:
    module.exports = devConfig;
    break;
}
