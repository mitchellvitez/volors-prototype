import { endpoints } from '../constants';

export default class Requests {
	
	static fetchPostLearn(input){
		return fetch(endpoints.LEARN, {
			method: 'post',
			body: JSON.stringify(input)
		})
	}
}