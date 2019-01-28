
def handle_change_status_desktop_approval_form(req):
    logger.info("handle_change_status_desktop_approval_form")
    # check permission
    if not is_admin_user(req['sender']):
        logger.error("only admin user have this permission.")
        return return_error(req, Error(ErrorCodes.PERMISSION_DENIED,
                                       ErrorMsg.ERR_MSG_ADMIN_USER_ONLY))

    # check must parameters
    for param in ['approval_id', 'status']:
        if param not in req or not req[param]:
            logger.error("[%s] not found in this request" % param)
            return return_error(req, Error(ErrorCodes.INVALID_REQUEST_FORMAT,
                                           ErrorMsg.ERR_MSG_MISSING_PARAMETER, param))

    approval_id = req.get('approval_id', '')
    status = req.get('status', '')

    if status not in [APPROVAL_FORM_STATUS_APPROVALING, APPROVAL_FORM_STATUS_EXIT]:
        return return_error(req, Error(ErrorCodes.INVALID_REQUEST_FORMAT,
                                       ErrorMsg.ERR_MSG_MISSING_PARAMETER, "status"))


    return return_success(req, {'approval_id': approval_id})