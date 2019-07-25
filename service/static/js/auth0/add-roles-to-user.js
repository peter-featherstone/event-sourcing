function (user, context, callback) {

  // Roles should only be set on verified users.
  if (!user.email || !user.email_verified) {
    return callback(null, user, context);
  }

  user.app_metadata = user.app_metadata || {};

  const addRolesToUser = function (user) {
    return context.authorization.roles;
  };

  const roles = addRolesToUser(user);
  const namespace = context.tenant;

  user.app_metadata.roles = roles;
  auth0.users.updateAppMetadata(user.user_id, user.app_metadata)
    .then(function () {
      context.idToken[`https://${namespace}/roles`] = user.app_metadata.roles;
      callback(null, user, context);
    })
    .catch(function (err) {
      callback(err);
    });
}
