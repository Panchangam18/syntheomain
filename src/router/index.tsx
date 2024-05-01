import { lazy, Suspense } from "react";
import { Switch, Route } from "react-router-dom";
import Header from "../components/Header";
import routes from "./config"; // Ensure this path is correct
import { Styles } from "../styles/styles";

const Router = () => {
  return (
    <Suspense fallback={<div>Loading...</div>}> 
      <Styles />
      <Header />
      <Switch>
        {routes.map((routeItem) => {
          return (
            <Route
              key={routeItem.component} // Key is the component name
              path={routeItem.path}
              exact={routeItem.exact}
              component={lazy(() => import(`../pages/${routeItem.component}`))} // Ensure path is correct
            />
          );
        })}
      </Switch>
    </Suspense>
  );
};

export default Router;
