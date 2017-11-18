import os
import testinfra.utils.ansible_runner

testinfra_hosts = testinfra.utils.ansible_runner.AnsibleRunner(
    os.environ['MOLECULE_INVENTORY_FILE']).get_hosts('all')


def test_sos_report_package(host):
    assert host.package("software-properties-common").is_installed
    apt_repo = int(host.check_output("find /etc/apt/ -type f -exec grep 'canonical-support/support-tools' '{}' \; -print | wc -l").strip())
    assert  apt_repo > 0
    assert host.package("sosreport").is_installed


def test_sos_report_file(host):
    assert host.check_output("find /tmp/sosreport-*/ -name 'sosreport-shoneslab*.tar.xz' | wc -l").strip() == '1'
