import React from 'react';
import { connect } from 'react-redux';
import Select from 'react-select';
import 'react-select/dist/react-select.css';

import { RouteActions } from '../actions';
import { routes } from '../constants';
import Requests from '../requests';

class PredictPage extends React.Component {

	constructor(){
		super();
		this.state = {};
		this.modelChange = this.modelChange.bind(this);
	}

	componentWillMount(){
		this.props.dispatch(RouteActions.setAppRoute(routes.PREDICT));

		Requests.getModels().then(response => {
			if (response.status == 200){

				response.json().then(models => {
					this.setState({ models });
				})

			} else {
				console.log('error getting models');
			}
			
		})
	}

	modelChange(selection){
		this.setState({currentSelection: selection});

		if (selection && selection.value){
			let model = selection.value;
			Requests.getHeaders(model).then(response => {
				if (response.status == 200){

					response.json().then(headers => {
						console.log(headers);
					})

				} else {
					console.log('error getting headers for ', model);
				}
			})
		}
		
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
								value={this.state.currentSelection}
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
