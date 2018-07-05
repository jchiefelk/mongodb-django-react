import React from 'react';
import { Route,  Switch } from 'react-router-dom';
import App from '../components/App';
import {hashHistory} from 'react-router';

const Routes = () => (
	  		<div>
	  			<Switch>
				    <Route exact path="/" component={App} />
		 		</Switch>
		    </div>
);

export default Routes;