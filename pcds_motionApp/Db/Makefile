TOP=../..
include $(TOP)/configure/CONFIG
#----------------------------------------
#  ADD MACRO DEFINITIONS AFTER THIS LINE

#----------------------------------------------------
#  Optimization of db files using dbst (DEFAULT: NO)
#DB_OPT = YES

#----------------------------------------------------
# Create and install (or just install)
# databases, templates, substitutions like this
DB += basic_motor_jt.template
DB += clinometer.template
DB += mcode.template
DB += motor-limit-aggregator.template
DB += motor-status.template
DB += motor-interlock.template
DB += pcds_motor.template
DB += pcds_motor_ims.template
DB += pcds_motor_test.template
DB += sim-valve.template
DB += sim-motor.template
DB += table-protection.template
DB += newall-shg-a2.template

DB += status_update.db

#
# Create and install archive templates and sample substitutions
#
ARCHIVE	+= archive_clinometer.tpl-arch
ARCHIVE	+= archive_motor.tpl-arch
ARCHIVE	+= archive_motor-mc.tpl-arch
ARCHIVE	+= archive_newall-shg-a2.tpl-arch

#
# Create and install autosave templates and sample substitutions
#
REQ	+= autosave_clinometer.tpl-req
REQ	+= autosave_motor_positions.tpl-req
REQ	+= autosave_motor_settings.tpl-req
REQ	+= autosave_motor_ilk.tpl-req
REQ	+= ims_motor_settings.tpl-req


include $(TOP)/configure/RULES
#----------------------------------------
#  ADD RULES AFTER THIS LINE

