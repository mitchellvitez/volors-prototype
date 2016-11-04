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

				<h1>Predict from Data</h1>
				<div style={{marginTop: '20px'}}></div>
				<div className="container">

					<div className="row">
						<p className="text-center">First you need to select a model:</p>
						<Select
								className="react-select"
								name="selectModels"
								placeholder="Select Model..."
								value={this.state.currentModel}
								options={options}
								onChange={this.modelChange}
						/>
					</div>
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
