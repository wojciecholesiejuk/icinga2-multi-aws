from icinga2_multi_aws import get_aws_instances

multiaws = get_aws_instances("/srv/icinga2-aws-multi-account-instance-discovery/config.json")
multiaws.update_aws_hosts()
multiaws.remove_terminated_instances()