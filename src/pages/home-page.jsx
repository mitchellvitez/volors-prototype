import React from 'react';
import { connect } from 'react-redux';

import { RouteActions } from '../actions';
import { routes } from '../constants';

class HomePage extends React.Component {
	componentWillMount(){
		this.props.dispatch(RouteActions.setAppRoute(routes.HOME));
	}

	render () {
		return (
			<div className="home-page">
				<div>
					<h1>Volors</h1>
					<h2 className="reduced-top-header">Better insights through machine learning, minus the programming</h2>
				</div>
				<br />
				<div>
					<p>Make the most of the information you have. Our goal is to make understanding and making predictions easy and convenient, no matter what shape your data takes.</p>
					<p>Signups will be opening soon. For now, try our <a href="learn">basic prediction tool</a>.</p>
					<p>&nbsp;</p>
					<form action="" method="">
						<p><input type="email" name="email" className="disabled" placeholder="email address" disabled/></p>
						<p><input type="submit" className="button disabled" name="submit" value="Sign up" disabled/></p>
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

export default connect(select)(HomePage);
