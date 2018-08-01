
ALTER TABLE  publish_publishapprovalhistory  ADD COLUMN  publish_sheet_id  integer NOT NULL;


ALTER TABLE  publish_publishapprovalhistory  ALTER COLUMN  publish_sheet_id  DROP DEFAULT;


ALTER TABLE  publish_publishapprovalhistory  ADD COLUMN  second_approver_id  integer NULL;


ALTER TABLE  publish_publishapprovalhistory  ALTER COLUMN  second_approver_id  DROP DEFAULT;


ALTER TABLE  publish_approver  ADD CONSTRAINT  publish_approver_approver_id_460c6774_fk_auth_user_id  FOREIGN KEY ( approver_id ) REFERENCES  auth_user  ( id );


ALTER TABLE  publish_projectinfo  ADD CONSTRAINT  publish_projectinfo_creator_id_2dad74a4_fk_auth_user_id  FOREIGN KEY ( creator_id ) REFERENCES  auth_user  ( id );


ALTER TABLE  publish_projectinfo  ADD CONSTRAINT  publish_projectinfo_group_id_4127d4d9_fk_asset_gogroup_id  FOREIGN KEY ( group_id ) REFERENCES  asset_gogroup  ( id );


ALTER TABLE  publish_projectinfo_first_approver  ADD CONSTRAINT  publish_projec_projectinfo_id_cfb69dee_fk_publish_projectinfo_id  FOREIGN KEY ( projectinfo_id ) REFERENCES  publish_projectinfo  ( id );


ALTER TABLE  publish_projectinfo_first_approver  ADD CONSTRAINT  publish_projectinfo_first_appro_user_id_c8cace54_fk_auth_user_id  FOREIGN KEY ( user_id ) REFERENCES  auth_user  ( id );


ALTER TABLE  publish_projectinfo_first_approver  ADD CONSTRAINT  publish_projectinfo_first_approver_projectinfo_id_dcd5b317_uniq  UNIQUE ( projectinfo_id ,  user_id );


ALTER TABLE  publish_projectinfo_mail_group  ADD CONSTRAINT  publish_projec_projectinfo_id_c9ff91f5_fk_publish_projectinfo_id  FOREIGN KEY ( projectinfo_id ) REFERENCES  publish_projectinfo  ( id );


ALTER TABLE  publish_projectinfo_mail_group  ADD CONSTRAINT  publish_projectinf_mailgroup_id_a74e5054_fk_publish_mailgroup_id  FOREIGN KEY ( mailgroup_id ) REFERENCES  publish_mailgroup  ( id );


ALTER TABLE  publish_projectinfo_mail_group  ADD CONSTRAINT  publish_projectinfo_mail_group_projectinfo_id_ce07ee2c_uniq  UNIQUE ( projectinfo_id ,  mailgroup_id );


ALTER TABLE  publish_projectinfo_owner  ADD CONSTRAINT  publish_projec_projectinfo_id_fd09201a_fk_publish_projectinfo_id  FOREIGN KEY ( projectinfo_id ) REFERENCES  publish_projectinfo  ( id );


ALTER TABLE  publish_projectinfo_owner  ADD CONSTRAINT  publish_projectinfo_owner_user_id_109233ca_fk_auth_user_id  FOREIGN KEY ( user_id ) REFERENCES  auth_user  ( id );


ALTER TABLE  publish_projectinfo_owner  ADD CONSTRAINT  publish_projectinfo_owner_projectinfo_id_4912124c_uniq  UNIQUE ( projectinfo_id ,  user_id );


ALTER TABLE  publish_projectinfo_second_approver  ADD CONSTRAINT  publish_projec_projectinfo_id_690dd63e_fk_publish_projectinfo_id  FOREIGN KEY ( projectinfo_id ) REFERENCES  publish_projectinfo  ( id );


ALTER TABLE  publish_projectinfo_second_approver  ADD CONSTRAINT  publish_projectinfo_second_appr_user_id_b1969421_fk_auth_user_id  FOREIGN KEY ( user_id ) REFERENCES  auth_user  ( id );


ALTER TABLE  publish_projectinfo_second_approver  ADD CONSTRAINT  publish_projectinfo_second_approver_projectinfo_id_2107cfa8_uniq  UNIQUE ( projectinfo_id ,  user_id );



ALTER TABLE  publish_publishapprovalhistory  ADD CONSTRAINT  publish_publishapprov_first_approver_id_0f82cdd0_fk_auth_user_id  FOREIGN KEY ( first_approver_id ) REFERENCES  auth_user  ( id );


ALTER TABLE  publish_publishsheet  ADD CONSTRAINT  publish_p_approval_level_id_2c0ffd36_fk_publish_approvallevel_id  FOREIGN KEY ( approval_level_id ) REFERENCES  publish_approvallevel  ( id );


ALTER TABLE  publish_publishsheet  ADD CONSTRAINT  publish_publishsheet_creator_id_8001628b_fk_auth_user_id  FOREIGN KEY ( creator_id ) REFERENCES  auth_user  ( id );


ALTER TABLE  publish_publishsheet_first_approver  ADD CONSTRAINT  publish_publ_publishsheet_id_0e70297e_fk_publish_publishsheet_id  FOREIGN KEY ( publishsheet_id ) REFERENCES  publish_publishsheet  ( id );


ALTER TABLE  publish_publishsheet_first_approver  ADD CONSTRAINT  publish_publishsheet_first_appr_user_id_f05891d0_fk_auth_user_id  FOREIGN KEY ( user_id ) REFERENCES  auth_user  ( id );


ALTER TABLE  publish_publishsheet_first_approver  ADD CONSTRAINT  publish_publishsheet_first_approve_publishsheet_id_df51741c_uniq  UNIQUE ( publishsheet_id ,  user_id );


ALTER TABLE  publish_publishsheet_goservices  ADD CONSTRAINT  publish_publ_publishsheet_id_198dafb0_fk_publish_publishsheet_id  FOREIGN KEY ( publishsheet_id ) REFERENCES  publish_publishsheet  ( id );


ALTER TABLE  publish_publishsheet_goservices  ADD CONSTRAINT  publish_publishshe_goservices_id_757cddf1_fk_asset_goservices_id  FOREIGN KEY ( goservices_id ) REFERENCES  asset_goservices  ( id );


ALTER TABLE  publish_publishsheet_goservices  ADD CONSTRAINT  publish_publishsheet_goservices_publishsheet_id_79897489_uniq  UNIQUE ( publishsheet_id ,  goservices_id );


ALTER TABLE  publish_publishsheet_qa  ADD CONSTRAINT  publish_publ_publishsheet_id_910a53b9_fk_publish_publishsheet_id  FOREIGN KEY ( publishsheet_id ) REFERENCES  publish_publishsheet  ( id );


ALTER TABLE  publish_publishsheet_qa  ADD CONSTRAINT  publish_publishsheet_qa_user_id_2fb19a81_fk_auth_user_id  FOREIGN KEY ( user_id ) REFERENCES  auth_user  ( id );


ALTER TABLE  publish_publishsheet_qa  ADD CONSTRAINT  publish_publishsheet_qa_publishsheet_id_c14bfddd_uniq  UNIQUE ( publishsheet_id ,  user_id );


ALTER TABLE  publish_publishsheet_reviewer  ADD CONSTRAINT  publish_publ_publishsheet_id_53d06fb2_fk_publish_publishsheet_id  FOREIGN KEY ( publishsheet_id ) REFERENCES  publish_publishsheet  ( id );


ALTER TABLE  publish_publishsheet_reviewer  ADD CONSTRAINT  publish_publishsheet_reviewer_user_id_7acb69f3_fk_auth_user_id  FOREIGN KEY ( user_id ) REFERENCES  auth_user  ( id );


ALTER TABLE  publish_publishsheet_reviewer  ADD CONSTRAINT  publish_publishsheet_reviewer_publishsheet_id_549fc3ac_uniq  UNIQUE ( publishsheet_id ,  user_id );


ALTER TABLE  publish_publishsheet_second_approver  ADD CONSTRAINT  publish_publ_publishsheet_id_835a33ad_fk_publish_publishsheet_id  FOREIGN KEY ( publishsheet_id ) REFERENCES  publish_publishsheet  ( id );


ALTER TABLE  publish_publishsheet_second_approver  ADD CONSTRAINT  publish_publishsheet_second_app_user_id_9aaa1151_fk_auth_user_id  FOREIGN KEY ( user_id ) REFERENCES  auth_user  ( id );


ALTER TABLE  publish_publishsheet_second_approver  ADD CONSTRAINT  publish_publishsheet_second_approv_publishsheet_id_5e27ee42_uniq  UNIQUE ( publishsheet_id ,  user_id );



ALTER TABLE  publish_timeslotlevel  ADD CONSTRAINT  publish_t_approval_level_id_908bbb69_fk_publish_approvallevel_id  FOREIGN KEY ( approval_level_id ) REFERENCES  publish_approvallevel  ( id );


ALTER TABLE  publish_timeslotlevel  ADD CONSTRAINT  publish_timeslotlevel_creator_id_9d04644f_fk_auth_user_id  FOREIGN KEY ( creator_id ) REFERENCES  auth_user  ( id );


CREATE INDEX  publish_publishapprovalhistory_77a408ad  ON  publish_publishapprovalhistory  ( publish_sheet_id );


ALTER TABLE  publish_publishapprovalhistory  ADD CONSTRAINT  publish_pub_publish_sheet_id_e33dfa2f_fk_publish_publishsheet_id  FOREIGN KEY ( publish_sheet_id ) REFERENCES  publish_publishsheet  ( id );


CREATE INDEX  publish_publishapprovalhistory_504db146  ON  publish_publishapprovalhistory  ( second_approver_id );


ALTER TABLE  publish_publishapprovalhistory  ADD CONSTRAINT  publish_publishappro_second_approver_id_5553529b_fk_auth_user_id  FOREIGN KEY ( second_approver_id ) REFERENCES  auth_user  ( id );


ALTER TABLE  publish_projectinfo_timeslot_level  ADD CONSTRAINT  publish_projec_projectinfo_id_96e120e9_fk_publish_projectinfo_id  FOREIGN KEY ( projectinfo_id ) REFERENCES  publish_projectinfo  ( id );


ALTER TABLE  publish_projectinfo_timeslot_level  ADD CONSTRAINT  publish_pr_timeslotlevel_id_9ccacb3c_fk_publish_timeslotlevel_id  FOREIGN KEY ( timeslotlevel_id ) REFERENCES  publish_timeslotlevel  ( id );


ALTER TABLE  publish_projectinfo_timeslot_level  ADD CONSTRAINT  publish_projectinfo_timeslot_level_projectinfo_id_3b3fcf91_uniq  UNIQUE ( projectinfo_id ,  timeslotlevel_id );

