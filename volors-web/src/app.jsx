import styles from './styles'; // eslint-disable-line no-unused-vars

import React from 'react'; // eslint-disable-line no-unused-vars
import { render } from 'react-dom';
import { Router, Route, browserHistory, IndexRoute } from 'react-router';
import { Provider } from 'react-redux';

import { routes } from './constants';
import store from './store';

import { 
		Navigator 
		,HomePage
		,LearnPage 
		,PredictPage
} from './pages';

render((
		<Provider store={store}>
			<Router history={browserHistory}>
				<Route path={routes.HOME} component={Navigator}>
					<IndexRoute component={HomePage} />
					<Route path={routes.LEARN} component={LearnPage} />
					<Route path={routes.PREDICT} component={PredictPage} />
				</Route>
			</Router>
		</Provider>
), document.getElementById('app'));
