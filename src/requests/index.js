import { endpoints } from '../constants';

export default class Requests {
	
	static postLearn(input){
		return fetch(endpoints.LEARN, {
			method: 'post',
			body: JSON.stringify(input)
		});
	}

	static getHeaders(model){
		return fetch(endpoints.HEADERS + '/' + model, {
			method: 'get'
		});
	}

	static getModels(){
		return fetch(endpoints.MODELS, {
			method: 'get'
		});
	}
}