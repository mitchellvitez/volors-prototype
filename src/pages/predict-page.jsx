import React from 'react';
import { connect } from 'react-redux';

import { RouteActions } from '../actions';
import { routes } from '../constants';

class PredictPage extends React.Component {
	componentWillMount(){
		this.props.dispatch(RouteActions.setAppRoute(routes.PREDICT));
	}

	render () {
		return (
			<div className="predict-page">
				<h1>Define features</h1>

				<p>Input a comma-separated list of features, and we'll tell you which classification the model predicts. Doesn't do input scrubbing, etc, therefore THIS IS NOT SECURE.</p>
				<p>Example well-formed data:</p>
				<p><code>5500,2.9</code></p>

				<div>
					<form method="POST" action="">
						<p><select name="model">
								<option value="filename">filename</option>
						</select></p>
						<p><input type="text" name="data" /></p>
						<p><input type="submit" className="button" value="submit"/></p>
					</form>
				</div>
			</div>
		);
	}
}

function select(state){
	return {
		currentRoute: state.currentRoute
	}
}

export default connect(select)(PredictPage);
