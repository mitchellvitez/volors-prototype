import { combineReducers } from 'redux';
import { currentRoute } from './current-route.js';

const rootReducer = combineReducers({
	currentRoute
})

export default rootReducer