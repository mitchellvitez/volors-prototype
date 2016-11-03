import React from 'react';
import { connect } from 'react-redux';

import { RouteActions } from '../actions';
import { routes } from '../constants';

class LearnPage extends React.Component {
	componentWillMount(){
		this.props.dispatch(RouteActions.setAppRoute(routes.LEARN));
	}

	render () {
		return (
			<div className="learn-page">
				<h1>Upload data</h1>
					<p>Make sure your first row has headers for your data, and the rightmost column contains the classes you want to group objects into. This sample only does classification problems, but we'll be adding more types of problems soon.</p>
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
					<form method="POST" action="" encType="multipart/form-data">
						<p>Upload CSV <input type="file" name="data"/></p>
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

export default connect(select)(LearnPage);
