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
		this.state = {
			hasSelected: false,
			data: {}
		};
		this.modelChange = this.modelChange.bind(this);
		this.preHasSelectedClass = this.preHasSelectedClass.bind(this);
		this.postHasSelectedClass = this.postHasSelectedClass.bind(this);
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
						
						this.setState({ headers });
						var data = {}
						for (var i in headers) data[headers[i]] = '';
						this.setState({
							data, 
							hasSelected: true
						});
						
					})

				} else {
					console.log('error getting headers for ', model);
				}
			})
		} else {
			this.setState({hasSelected: false});
		}
	}

	preHasSelectedClass(){
		return this.state.hasSelected ? ' display-none' : '';
	}

	postHasSelectedClass(){
		return !this.state.hasSelected ? ' display-none' : '';
	}

	changeData(e, header){
		var data = this.state.data;
		data[header] = e.target.value;
		this.setState({data})
		console.log(this.state.data)
	}

	render () {

		let models = this.state.models || []
		let options = models.map((model) => {
			return {
				value: model,
				label: model
			}
		})
		let headers = this.state.headers || []

		return (
			<div className="predict-page">

				<h1>Predict from Data</h1>
				<div className="container" style={{marginTop: '50px'}}>
					<div className="row">
						<p className={'text-center'+this.preHasSelectedClass()}>First you need to select a model:</p>
						<p className={'text-center'+this.postHasSelectedClass()}>selected model:</p>
						<Select
								className="react-select"
								name="selectModels"
								placeholder="Select Model..."
								value={this.state.currentSelection}
								options={options}
								onChange={this.modelChange}
						/>
					</div>
					<div className={'row'+this.postHasSelectedClass()} style={{marginTop: '50px'}}>
						{headers.map((header, index) => {
							return (
								<div key={index} className="col-xs-12 col-sm-4">
									<label style={{marginLeft: '10px', marginRight: '10px', marginBottom: '0px'}}>{header}</label>
									<input type="text" value={this.state.data[header]} onChange={e => {return this.changeData(e, header)}}/>
								</div>
							)
						})}
						<button className="input-button" style={{marginTop: '30px'}}>submit</button>
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
