import React from 'react';
import { connect } from 'react-redux';
import Select from 'react-select';
import 'react-select/dist/react-select.css';

import { RouteActions } from '../actions';
import { routes } from '../constants';

class PredictPage extends React.Component {

	constructor(){
		super();
		let models = ['Animal', 'Food', 'Sport', 'Movie'];
		this.state = {
			models
		};
		this.modelChange = this.modelChange.bind(this);
	}

	componentWillMount(){
		this.props.dispatch(RouteActions.setAppRoute(routes.PREDICT));
	}

	modelChange(val){
		console.log(val)
		this.setState({currentModel: val});
	}

	render () {

		let models = this.state.models || []
		let options = models.map((model) => {
			return {
				value: model,
				label: model
			}
		})

		return (
			<div className="predict-page">
				<h1>Define features</h1>

				<p>Input a comma-separated list of features, and we'll tell you which classification the model predicts. Doesn't do input scrubbing, etc, therefore THIS IS NOT SECURE.</p>
				<p>Example well-formed data:</p>
				<p><code>5500,2.9</code></p>

				<div>
					<form>
						<Select
								className="react-select"
								name="selectModels"
								value={this.state.currentModel}
								options={options}
								onChange={this.modelChange}
						/>
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
