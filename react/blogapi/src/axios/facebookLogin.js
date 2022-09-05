import axios from 'axios';
import { useHistory } from 'react-router-dom';

const facebookLogin = (accesstoken) => {
	console.log(accesstoken);
	axios
		.post('http://127.0.0.1:8000/auth/convert-token', {
			token: accesstoken,
			backend: 'facebook',
			grant_type: 'convert_token',
			client_id: 'G79JmW7cygQH89AnOo78RfiizcTIm9ClllhHO1mp',
			client_secret:
				'9aKW4wbCQjK912z4g81ZM64AGaRcPuLzF0hvAn8NfINaFhwRkihXxlGdjKoaVh00AKuzr1kIDQF0vKklyOiVXwoRlRlwx3B4tz9ZKFpaRcHnlDTYihewBfUHNhbcPGX6',
		})
		.then((res) => {
			localStorage.setItem('access_token', res.data.access_token);
			localStorage.setItem('refresh_token', res.data.refresh_token);
		});
};

export default facebookLogin;
