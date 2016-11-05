import React from 'react';
import { connect } from 'react-redux';

import { RouteActions } from '../actions';
import { routes } from '../constants';
import Requests from '../requests';

class LearnPage extends React.Component {

	constructor(){
		super();
		this.state = {};
		this.uploadFile = this.uploadFile.bind(this);
		this.setStartedUpload = this.setStartedUpload.bind(this);
		this.submitData = this.submitData.bind(this);
	}

	componentWillMount(){
		this.props.dispatch(RouteActions.setAppRoute(routes.LEARN));
	}

	uploadFile(e) {
		e.preventDefault();

		let reader = new FileReader();
		let file = e.target.files[0];

		// save file into state (both encoded URL and file)
		reader.onloadend = (fileLoadedEvent) => {
			let encoded = fileLoadedEvent.target.result;
			this.setState({
				file: file,
				encoded: encoded
			});
			this.setState({started: false})
		}
		reader.readAsDataURL(file)
	}

	setStartedUpload(){
		this.setState({started: true})
	}

	submitData(){
		if (this.state && this.state.encoded){
			Requests.postLearn(this.state.encoded).then(response => {
				if (response.status == 200){
					response.json().then(model => {
						console.log(model)
					});
				} else {
					console.log('error posting file');
				}
			});
		}
	}

	render () {
		return (
			<div className="learn-page">
				<h1>Upload data</h1>
				<div style={{marginTop: '20px'}}></div>
				<div className="container">
					<p>
						Make sure your first row has headers for your data, 
						and the rightmost column contains the classes you want to group objects into. 
						This sample only does classification problems, 
						but we'll be adding more types of problems soon.
					</p>
					<p>Example well-formed data:</p>

				<div className="content">
					<table>
						<tbody>
							<tr>
								<th>Weight (kg)</th>
								<th>Height (m)</th>
							<th>Animal</th>
							</tr>
							<tr>
								<td>6000</td>
								<td>3.1</td>
								<td>elephant</td>
							</tr>
							<tr>
								<td>.04</td>
								<td>.1</td>
								<td>mouse</td>
							</tr>
							<tr>
								<td>5600</td>
								<td>2.5</td>
								<td>elephant</td>
							</tr>
						</tbody>
					</table>
				</div>

				<div>
					<form>
						<p>Upload CSV</p>
						<input type="file" name="data" onClick={this.setStartedUpload} 
								onChange={(e) => {this.uploadFile(e)}}/>
					</form>
					<button className="input-button" onClick={this.submitData}>submit</button>
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

export default connect(select)(LearnPage);
