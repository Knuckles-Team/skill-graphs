#  Debian Reference
### Osamu Aoki
Copyright © 2007-2012 Osamu Aoki
This Debian Reference (v2) (2012-07-11 04:20:12 UTC) is intended to provide a broad overview of the Debian system as a post-installation user's guide. It covers many aspects of system administration through shell-command examples for non-developers.
**Abstract**
This book is free; you may redistribute it and/or modify it under the terms of the GNU General Public License of any version compliant to the Debian Free Software Guidelines (DFSG).
* * *
**Table of Contents**

[Preface](https://tldp.org/LDP/www.debian.org/doc/manuals/debian-reference/pr01.en.html)


[1. Disclaimer](https://tldp.org/LDP/www.debian.org/doc/manuals/debian-reference/pr01.en.html#_disclaimer)


[2. What is Debian](https://tldp.org/LDP/www.debian.org/doc/manuals/debian-reference/pr01.en.html#_what_is_debian)


[3. About this document](https://tldp.org/LDP/www.debian.org/doc/manuals/debian-reference/pr01.en.html#_about_this_document)


[3.1. Guiding rules](https://tldp.org/LDP/www.debian.org/doc/manuals/debian-reference/pr01.en.html#_guiding_rules)


[3.2. Prerequisites](https://tldp.org/LDP/www.debian.org/doc/manuals/debian-reference/pr01.en.html#_prerequisites)


[3.3. Conventions](https://tldp.org/LDP/www.debian.org/doc/manuals/debian-reference/pr01.en.html#_conventions)


[3.4. The popcon](https://tldp.org/LDP/www.debian.org/doc/manuals/debian-reference/pr01.en.html#_the_popcon)


[3.5. The package size](https://tldp.org/LDP/www.debian.org/doc/manuals/debian-reference/pr01.en.html#_the_package_size)


[3.6. Bug reports on this document](https://tldp.org/LDP/www.debian.org/doc/manuals/debian-reference/pr01.en.html#_bug_reports_on_this_document)


[4. Some quotes for new users](https://tldp.org/LDP/www.debian.org/doc/manuals/debian-reference/pr01.en.html#_some_quotes_for_new_users)


[1. GNU/Linux tutorials](https://tldp.org/LDP/www.debian.org/doc/manuals/debian-reference/ch01.en.html)


[1.1. Console basics](https://tldp.org/LDP/www.debian.org/doc/manuals/debian-reference/ch01.en.html#_console_basics)


[1.1.1. The shell prompt](https://tldp.org/LDP/www.debian.org/doc/manuals/debian-reference/ch01.en.html#_the_shell_prompt)


[1.1.2. The shell prompt under X](https://tldp.org/LDP/www.debian.org/doc/manuals/debian-reference/ch01.en.html#_the_shell_prompt_under_x)


[1.1.3. The root account](https://tldp.org/LDP/www.debian.org/doc/manuals/debian-reference/ch01.en.html#_the_root_account)


[1.1.4. The root shell prompt](https://tldp.org/LDP/www.debian.org/doc/manuals/debian-reference/ch01.en.html#_the_root_shell_prompt)


[1.1.5. GUI system administration tools](https://tldp.org/LDP/www.debian.org/doc/manuals/debian-reference/ch01.en.html#_gui_system_administration_tools)


[1.1.6. Virtual consoles](https://tldp.org/LDP/www.debian.org/doc/manuals/debian-reference/ch01.en.html#_virtual_consoles)


[1.1.7. How to leave the command prompt](https://tldp.org/LDP/www.debian.org/doc/manuals/debian-reference/ch01.en.html#_how_to_leave_the_command_prompt)


[1.1.8. How to shutdown the system](https://tldp.org/LDP/www.debian.org/doc/manuals/debian-reference/ch01.en.html#_how_to_shutdown_the_system)


[1.1.9. Recovering a sane console](https://tldp.org/LDP/www.debian.org/doc/manuals/debian-reference/ch01.en.html#_recovering_a_sane_console)


[1.1.10. Additional package suggestions for the newbie](https://tldp.org/LDP/www.debian.org/doc/manuals/debian-reference/ch01.en.html#_additional_package_suggestions_for_the_newbie)


[1.1.11. An extra user account](https://tldp.org/LDP/www.debian.org/doc/manuals/debian-reference/ch01.en.html#_an_extra_user_account)


[1.1.12. sudo configuration](https://tldp.org/LDP/www.debian.org/doc/manuals/debian-reference/ch01.en.html#_sudo_configuration)


[1.1.13. Play time](https://tldp.org/LDP/www.debian.org/doc/manuals/debian-reference/ch01.en.html#_play_time)


[1.2. Unix-like filesystem](https://tldp.org/LDP/www.debian.org/doc/manuals/debian-reference/ch01.en.html#_unix_like_filesystem)


[1.2.1. Unix file basics](https://tldp.org/LDP/www.debian.org/doc/manuals/debian-reference/ch01.en.html#_unix_file_basics)


[1.2.2. Filesystem internals](https://tldp.org/LDP/www.debian.org/doc/manuals/debian-reference/ch01.en.html#_filesystem_internals)


[1.2.3. Filesystem permissions](https://tldp.org/LDP/www.debian.org/doc/manuals/debian-reference/ch01.en.html#_filesystem_permissions)


[1.2.4. Control of permissions for newly created files: umask](https://tldp.org/LDP/www.debian.org/doc/manuals/debian-reference/ch01.en.html#_control_of_permissions_for_newly_created_files_umask)


[1.2.5. Permissions for groups of users (group)](https://tldp.org/LDP/www.debian.org/doc/manuals/debian-reference/ch01.en.html#_permissions_for_groups_of_users_group)


[1.2.6. Timestamps](https://tldp.org/LDP/www.debian.org/doc/manuals/debian-reference/ch01.en.html#_timestamps)


[1.2.7. Links](https://tldp.org/LDP/www.debian.org/doc/manuals/debian-reference/ch01.en.html#_links)


[1.2.8. Named pipes (FIFOs)](https://tldp.org/LDP/www.debian.org/doc/manuals/debian-reference/ch01.en.html#_named_pipes_fifos)


[1.2.9. Sockets](https://tldp.org/LDP/www.debian.org/doc/manuals/debian-reference/ch01.en.html#_sockets)


[1.2.10. Device files](https://tldp.org/LDP/www.debian.org/doc/manuals/debian-reference/ch01.en.html#_device_files)


[1.2.11. Special device files](https://tldp.org/LDP/www.debian.org/doc/manuals/debian-reference/ch01.en.html#_special_device_files)


[1.2.12. procfs and sysfs](https://tldp.org/LDP/www.debian.org/doc/manuals/debian-reference/ch01.en.html#_procfs_and_sysfs)


[1.2.13. tmpfs](https://tldp.org/LDP/www.debian.org/doc/manuals/debian-reference/ch01.en.html#_tmpfs)


[1.3. Midnight Commander (MC)](https://tldp.org/LDP/www.debian.org/doc/manuals/debian-reference/ch01.en.html#_midnight_commander_mc)


[1.3.1. Customization of MC](https://tldp.org/LDP/www.debian.org/doc/manuals/debian-reference/ch01.en.html#_customization_of_mc)


[1.3.2. Starting MC](https://tldp.org/LDP/www.debian.org/doc/manuals/debian-reference/ch01.en.html#_starting_mc)


[1.3.3. File manager in MC](https://tldp.org/LDP/www.debian.org/doc/manuals/debian-reference/ch01.en.html#_file_manager_in_mc)


[1.3.4. Command-line tricks in MC](https://tldp.org/LDP/www.debian.org/doc/manuals/debian-reference/ch01.en.html#_command_line_tricks_in_mc)


[1.3.5. The internal editor in MC](https://tldp.org/LDP/www.debian.org/doc/manuals/debian-reference/ch01.en.html#_the_internal_editor_in_mc)


[1.3.6. The internal viewer in MC](https://tldp.org/LDP/www.debian.org/doc/manuals/debian-reference/ch01.en.html#_the_internal_viewer_in_mc)


[1.3.7. Auto-start features of MC](https://tldp.org/LDP/www.debian.org/doc/manuals/debian-reference/ch01.en.html#_auto_start_features_of_mc)


[1.3.8. FTP virtual filesystem of MC](https://tldp.org/LDP/www.debian.org/doc/manuals/debian-reference/ch01.en.html#_ftp_virtual_filesystem_of_mc)


[1.4. The basic Unix-like work environment](https://tldp.org/LDP/www.debian.org/doc/manuals/debian-reference/ch01.en.html#_the_basic_unix_like_work_environment)


[1.4.1. The login shell](https://tldp.org/LDP/www.debian.org/doc/manuals/debian-reference/ch01.en.html#_the_login_shell)


[1.4.2. Customizing bash](https://tldp.org/LDP/www.debian.org/doc/manuals/debian-reference/ch01.en.html#_customizing_bash)


[1.4.3. Special key strokes](https://tldp.org/LDP/www.debian.org/doc/manuals/debian-reference/ch01.en.html#_special_key_strokes)


[1.4.4. Unix style mouse operations](https://tldp.org/LDP/www.debian.org/doc/manuals/debian-reference/ch01.en.html#_unix_style_mouse_operations)


[1.4.5. The pager](https://tldp.org/LDP/www.debian.org/doc/manuals/debian-reference/ch01.en.html#_the_pager)


[1.4.6. The text editor](https://tldp.org/LDP/www.debian.org/doc/manuals/debian-reference/ch01.en.html#_the_text_editor)


[1.4.7. Setting a default text editor](https://tldp.org/LDP/www.debian.org/doc/manuals/debian-reference/ch01.en.html#_setting_a_default_text_editor)


[1.4.8. Customizing vim](https://tldp.org/LDP/www.debian.org/doc/manuals/debian-reference/ch01.en.html#_customizing_vim)


[1.4.9. Recording the shell activities](https://tldp.org/LDP/www.debian.org/doc/manuals/debian-reference/ch01.en.html#_recording_the_shell_activities)


[1.4.10. Basic Unix commands](https://tldp.org/LDP/www.debian.org/doc/manuals/debian-reference/ch01.en.html#_basic_unix_commands)


[1.5. The simple shell command](https://tldp.org/LDP/www.debian.org/doc/manuals/debian-reference/ch01.en.html#_the_simple_shell_command)


[1.5.1. Command execution and environment variable](https://tldp.org/LDP/www.debian.org/doc/manuals/debian-reference/ch01.en.html#_command_execution_and_environment_variable)


[1.5.2. "`$LANG`" variable](https://tldp.org/LDP/www.debian.org/doc/manuals/debian-reference/ch01.en.html#_literal_lang_literal_variable)


[1.5.3. "`$PATH`" variable](https://tldp.org/LDP/www.debian.org/doc/manuals/debian-reference/ch01.en.html#_literal_path_literal_variable)


[1.5.4. "`$HOME`" variable](https://tldp.org/LDP/www.debian.org/doc/manuals/debian-reference/ch01.en.html#_literal_home_literal_variable)


[1.5.5. Command line options](https://tldp.org/LDP/www.debian.org/doc/manuals/debian-reference/ch01.en.html#_command_line_options)


[1.5.6. Shell glob](https://tldp.org/LDP/www.debian.org/doc/manuals/debian-reference/ch01.en.html#_shell_glob)


[1.5.7. Return value of the command](https://tldp.org/LDP/www.debian.org/doc/manuals/debian-reference/ch01.en.html#_return_value_of_the_command)


[1.5.8. Typical command sequences and shell redirection](https://tldp.org/LDP/www.debian.org/doc/manuals/debian-reference/ch01.en.html#_typical_command_sequences_and_shell_redirection)


[1.5.9. Command alias](https://tldp.org/LDP/www.debian.org/doc/manuals/debian-reference/ch01.en.html#_command_alias)


[1.6. Unix-like text processing](https://tldp.org/LDP/www.debian.org/doc/manuals/debian-reference/ch01.en.html#_unix_like_text_processing)


[1.6.1. Unix text tools](https://tldp.org/LDP/www.debian.org/doc/manuals/debian-reference/ch01.en.html#_unix_text_tools)


[1.6.2. Regular expressions](https://tldp.org/LDP/www.debian.org/doc/manuals/debian-reference/ch01.en.html#_regular_expressions)


[1.6.3. Replacement expressions](https://tldp.org/LDP/www.debian.org/doc/manuals/debian-reference/ch01.en.html#_replacement_expressions)


[1.6.4. Global substitution with regular expressions](https://tldp.org/LDP/www.debian.org/doc/manuals/debian-reference/ch01.en.html#_global_substitution_with_regular_expressions)


[1.6.5. Extracting data from text file table](https://tldp.org/LDP/www.debian.org/doc/manuals/debian-reference/ch01.en.html#_extracting_data_from_text_file_table)


[1.6.6. Script snippets for piping commands](https://tldp.org/LDP/www.debian.org/doc/manuals/debian-reference/ch01.en.html#_script_snippets_for_piping_commands)


[2. Debian package management](https://tldp.org/LDP/www.debian.org/doc/manuals/debian-reference/ch02.en.html)


[2.1. Debian package management prerequisites](https://tldp.org/LDP/www.debian.org/doc/manuals/debian-reference/ch02.en.html#_debian_package_management_prerequisites)


[2.1.1. Package configuration](https://tldp.org/LDP/www.debian.org/doc/manuals/debian-reference/ch02.en.html#_package_configuration)


[2.1.2. Basic precautions](https://tldp.org/LDP/www.debian.org/doc/manuals/debian-reference/ch02.en.html#_basic_precautions)


[2.1.3. Life with eternal upgrades](https://tldp.org/LDP/www.debian.org/doc/manuals/debian-reference/ch02.en.html#_life_with_eternal_upgrades)


[2.1.4. Debian archive basics](https://tldp.org/LDP/www.debian.org/doc/manuals/debian-reference/ch02.en.html#_debian_archive_basics)


[2.1.5. Package dependencies](https://tldp.org/LDP/www.debian.org/doc/manuals/debian-reference/ch02.en.html#_package_dependencies)


[2.1.6. The event flow of the package management](https://tldp.org/LDP/www.debian.org/doc/manuals/debian-reference/ch02.en.html#_the_event_flow_of_the_package_management)


[2.1.7. First response to package management troubles](https://tldp.org/LDP/www.debian.org/doc/manuals/debian-reference/ch02.en.html#_first_response_to_package_management_troubles)


[2.2. Basic package management operations](https://tldp.org/LDP/www.debian.org/doc/manuals/debian-reference/ch02.en.html#_basic_package_management_operations)


[2.2.1. `apt-get` / `apt-cache` vs. `aptitude`](https://tldp.org/LDP/www.debian.org/doc/manuals/debian-reference/ch02.en.html#_literal_apt_get_literal_literal_apt_cache_literal_vs_literal_aptitude_literal)


[2.2.2. Basic package management operations with the commandline](https://tldp.org/LDP/www.debian.org/doc/manuals/debian-reference/ch02.en.html#_basic_package_management_operations_with_the_commandline)


[2.2.3. Interactive use of aptitude](https://tldp.org/LDP/www.debian.org/doc/manuals/debian-reference/ch02.en.html#_interactive_use_of_aptitude)


[2.2.4. Key bindings of aptitude](https://tldp.org/LDP/www.debian.org/doc/manuals/debian-reference/ch02.en.html#_key_bindings_of_aptitude)


[2.2.5. Package views under aptitude](https://tldp.org/LDP/www.debian.org/doc/manuals/debian-reference/ch02.en.html#_package_views_under_aptitude)


[2.2.6. Search method options with aptitude](https://tldp.org/LDP/www.debian.org/doc/manuals/debian-reference/ch02.en.html#_search_method_options_with_aptitude)


[2.2.7. The aptitude regex formula](https://tldp.org/LDP/www.debian.org/doc/manuals/debian-reference/ch02.en.html#_the_aptitude_regex_formula)


[2.2.8. Dependency resolution of aptitude](https://tldp.org/LDP/www.debian.org/doc/manuals/debian-reference/ch02.en.html#_dependency_resolution_of_aptitude)


[2.2.9. Package activity logs](https://tldp.org/LDP/www.debian.org/doc/manuals/debian-reference/ch02.en.html#_package_activity_logs)


[2.3. Examples of aptitude operations](https://tldp.org/LDP/www.debian.org/doc/manuals/debian-reference/ch02.en.html#_examples_of_aptitude_operations)


[2.3.1. Listing packages with regex matching on package names](https://tldp.org/LDP/www.debian.org/doc/manuals/debian-reference/ch02.en.html#_listing_packages_with_regex_matching_on_package_names)


[2.3.2. Browsing with the regex matching](https://tldp.org/LDP/www.debian.org/doc/manuals/debian-reference/ch02.en.html#_browsing_with_the_regex_matching)


[2.3.3. Purging removed packages for good](https://tldp.org/LDP/www.debian.org/doc/manuals/debian-reference/ch02.en.html#_purging_removed_packages_for_good)


[2.3.4. Tidying auto/manual install status](https://tldp.org/LDP/www.debian.org/doc/manuals/debian-reference/ch02.en.html#_tidying_auto_manual_install_status)


[2.3.5. System wide upgrade](https://tldp.org/LDP/www.debian.org/doc/manuals/debian-reference/ch02.en.html#_system_wide_upgrade)


[2.4. Advanced package management operations](https://tldp.org/LDP/www.debian.org/doc/manuals/debian-reference/ch02.en.html#_advanced_package_management_operations)


[2.4.1. Advanced package management operations with commandline](https://tldp.org/LDP/www.debian.org/doc/manuals/debian-reference/ch02.en.html#_advanced_package_management_operations_with_commandline)


[2.4.2. Verification of installed package files](https://tldp.org/LDP/www.debian.org/doc/manuals/debian-reference/ch02.en.html#_verification_of_installed_package_files)


[2.4.3. Safeguarding for package problems](https://tldp.org/LDP/www.debian.org/doc/manuals/debian-reference/ch02.en.html#_safeguarding_for_package_problems)


[2.4.4. Searching on the package meta data](https://tldp.org/LDP/www.debian.org/doc/manuals/debian-reference/ch02.en.html#_searching_on_the_package_meta_data)


[2.5. Debian package management internals](https://tldp.org/LDP/www.debian.org/doc/manuals/debian-reference/ch02.en.html#_debian_package_management_internals)


[2.5.1. Archive meta data](https://tldp.org/LDP/www.debian.org/doc/manuals/debian-reference/ch02.en.html#_archive_meta_data)


[2.5.2. Top level "Release" file and authenticity](https://tldp.org/LDP/www.debian.org/doc/manuals/debian-reference/ch02.en.html#_top_level_release_file_and_authenticity)


[2.5.3. Archive level "Release" files](https://tldp.org/LDP/www.debian.org/doc/manuals/debian-reference/ch02.en.html#_archive_level_release_files)


[2.5.4. Fetching of the meta data for the package](https://tldp.org/LDP/www.debian.org/doc/manuals/debian-reference/ch02.en.html#_fetching_of_the_meta_data_for_the_package)


[2.5.5. The package state for APT](https://tldp.org/LDP/www.debian.org/doc/manuals/debian-reference/ch02.en.html#_the_package_state_for_apt)


[2.5.6. The package state for aptitude](https://tldp.org/LDP/www.debian.org/doc/manuals/debian-reference/ch02.en.html#_the_package_state_for_aptitude)


[2.5.7. Local copies of the fetched packages](https://tldp.org/LDP/www.debian.org/doc/manuals/debian-reference/ch02.en.html#_local_copies_of_the_fetched_packages)


[2.5.8. Debian package file names](https://tldp.org/LDP/www.debian.org/doc/manuals/debian-reference/ch02.en.html#_debian_package_file_names)


[2.5.9. The dpkg command](https://tldp.org/LDP/www.debian.org/doc/manuals/debian-reference/ch02.en.html#_the_dpkg_command)


[2.5.10. The update-alternative command](https://tldp.org/LDP/www.debian.org/doc/manuals/debian-reference/ch02.en.html#_the_update_alternative_command)


[2.5.11. The dpkg-statoverride command](https://tldp.org/LDP/www.debian.org/doc/manuals/debian-reference/ch02.en.html#_the_dpkg_statoverride_command)


[2.5.12. The dpkg-divert command](https://tldp.org/LDP/www.debian.org/doc/manuals/debian-reference/ch02.en.html#_the_dpkg_divert_command)


[2.6. Recovery from a broken system](https://tldp.org/LDP/www.debian.org/doc/manuals/debian-reference/ch02.en.html#_recovery_from_a_broken_system)


[2.6.1. Incompatibility with old user configuration](https://tldp.org/LDP/www.debian.org/doc/manuals/debian-reference/ch02.en.html#_incompatibility_with_old_user_configuration)


[2.6.2. Different packages with overlapped files](https://tldp.org/LDP/www.debian.org/doc/manuals/debian-reference/ch02.en.html#_different_packages_with_overlapped_files)


[2.6.3. Fixing broken package script](https://tldp.org/LDP/www.debian.org/doc/manuals/debian-reference/ch02.en.html#_fixing_broken_package_script)


[2.6.4. Rescue with the dpkg command](https://tldp.org/LDP/www.debian.org/doc/manuals/debian-reference/ch02.en.html#_rescue_with_the_dpkg_command)


[2.6.5. Recovering package selection data](https://tldp.org/LDP/www.debian.org/doc/manuals/debian-reference/ch02.en.html#_recovering_package_selection_data)


[2.7. Tips for the package management](https://tldp.org/LDP/www.debian.org/doc/manuals/debian-reference/ch02.en.html#_tips_for_the_package_management)


[2.7.1. How to pick Debian packages](https://tldp.org/LDP/www.debian.org/doc/manuals/debian-reference/ch02.en.html#_how_to_pick_debian_packages)


[2.7.2. Packages from mixed source of archives](https://tldp.org/LDP/www.debian.org/doc/manuals/debian-reference/ch02.en.html#_packages_from_mixed_source_of_archives)


[2.7.3. Tweaking candidate version](https://tldp.org/LDP/www.debian.org/doc/manuals/debian-reference/ch02.en.html#_tweaking_candidate_version)


[2.7.4. Updates and Backports](https://tldp.org/LDP/www.debian.org/doc/manuals/debian-reference/ch02.en.html#_updates_and_backports)


[2.7.5. Blocking packages installed by "Recommends"](https://tldp.org/LDP/www.debian.org/doc/manuals/debian-reference/ch02.en.html#_blocking_packages_installed_by_recommends)


[2.7.6. Tracking `testing` with some packages from `unstable`](https://tldp.org/LDP/www.debian.org/doc/manuals/debian-reference/ch02.en.html#_tracking_literal_testing_literal_with_some_packages_from_literal_unstable_literal)


[2.7.7. Tracking `unstable` with some packages from `experimental`](https://tldp.org/LDP/www.debian.org/doc/manuals/debian-reference/ch02.en.html#_tracking_literal_unstable_literal_with_some_packages_from_literal_experimental_literal)


[2.7.8. Automatic download and upgrade of packages](https://tldp.org/LDP/www.debian.org/doc/manuals/debian-reference/ch02.en.html#_automatic_download_and_upgrade_of_packages)


[2.7.9. Limiting download bandwidth for APT](https://tldp.org/LDP/www.debian.org/doc/manuals/debian-reference/ch02.en.html#_limiting_download_bandwidth_for_apt)


[2.7.10. Emergency downgrading](https://tldp.org/LDP/www.debian.org/doc/manuals/debian-reference/ch02.en.html#_emergency_downgrading)


[2.7.11. Who uploaded the package?](https://tldp.org/LDP/www.debian.org/doc/manuals/debian-reference/ch02.en.html#_who_uploaded_the_package)


[2.7.12. The equivs package](https://tldp.org/LDP/www.debian.org/doc/manuals/debian-reference/ch02.en.html#_the_equivs_package)


[2.7.13. Porting a package to the stable system](https://tldp.org/LDP/www.debian.org/doc/manuals/debian-reference/ch02.en.html#_porting_a_package_to_the_stable_system)


[2.7.14. Proxy server for APT](https://tldp.org/LDP/www.debian.org/doc/manuals/debian-reference/ch02.en.html#_proxy_server_for_apt)


[2.7.15. Small public package archive](https://tldp.org/LDP/www.debian.org/doc/manuals/debian-reference/ch02.en.html#_small_public_package_archive)


[2.7.16. Recording and copying system configuration](https://tldp.org/LDP/www.debian.org/doc/manuals/debian-reference/ch02.en.html#_recording_and_copying_system_configuration)


[2.7.17. Converting or installing an alien binary package](https://tldp.org/LDP/www.debian.org/doc/manuals/debian-reference/ch02.en.html#_converting_or_installing_an_alien_binary_package)


[2.7.18. Extracting package without dpkg](https://tldp.org/LDP/www.debian.org/doc/manuals/debian-reference/ch02.en.html#_extracting_package_without_dpkg)


[2.7.19. More readings for the package management](https://tldp.org/LDP/www.debian.org/doc/manuals/debian-reference/ch02.en.html#_more_readings_for_the_package_management)


[3. The system initialization](https://tldp.org/LDP/www.debian.org/doc/manuals/debian-reference/ch03.en.html)


[3.1. An overview of the boot strap process](https://tldp.org/LDP/www.debian.org/doc/manuals/debian-reference/ch03.en.html#_an_overview_of_the_boot_strap_process)


[3.2. Stage 1: the BIOS](https://tldp.org/LDP/www.debian.org/doc/manuals/debian-reference/ch03.en.html#_stage_1_the_bios)


[3.3. Stage 2: the boot loader](https://tldp.org/LDP/www.debian.org/doc/manuals/debian-reference/ch03.en.html#_stage_2_the_boot_loader)


[3.4. Stage 3: the mini-Debian system](https://tldp.org/LDP/www.debian.org/doc/manuals/debian-reference/ch03.en.html#_stage_3_the_mini_debian_system)


[3.5. Stage 4: the normal Debian system](https://tldp.org/LDP/www.debian.org/doc/manuals/debian-reference/ch03.en.html#_stage_4_the_normal_debian_system)


[3.5.1. The meaning of the runlevel](https://tldp.org/LDP/www.debian.org/doc/manuals/debian-reference/ch03.en.html#_the_meaning_of_the_runlevel)


[3.5.2. The configuration of the runlevel](https://tldp.org/LDP/www.debian.org/doc/manuals/debian-reference/ch03.en.html#_the_configuration_of_the_runlevel)


[3.5.3. The runlevel management example](https://tldp.org/LDP/www.debian.org/doc/manuals/debian-reference/ch03.en.html#_the_runlevel_management_example)


[3.5.4. The default parameter for each init script](https://tldp.org/LDP/www.debian.org/doc/manuals/debian-reference/ch03.en.html#_the_default_parameter_for_each_init_script)


[3.5.5. The hostname](https://tldp.org/LDP/www.debian.org/doc/manuals/debian-reference/ch03.en.html#_the_hostname)


[3.5.6. The filesystem](https://tldp.org/LDP/www.debian.org/doc/manuals/debian-reference/ch03.en.html#_the_filesystem)


[3.5.7. Network interface initialization](https://tldp.org/LDP/www.debian.org/doc/manuals/debian-reference/ch03.en.html#_network_interface_initialization)


[3.5.8. Network service initialization](https://tldp.org/LDP/www.debian.org/doc/manuals/debian-reference/ch03.en.html#_network_service_initialization)


[3.5.9. The system message](https://tldp.org/LDP/www.debian.org/doc/manuals/debian-reference/ch03.en.html#_the_system_message)


[3.5.10. The kernel message](https://tldp.org/LDP/www.debian.org/doc/manuals/debian-reference/ch03.en.html#_the_kernel_message)


[3.5.11. The udev system](https://tldp.org/LDP/www.debian.org/doc/manuals/debian-reference/ch03.en.html#_the_udev_system)


[3.5.12. The kernel module initialization](https://tldp.org/LDP/www.debian.org/doc/manuals/debian-reference/ch03.en.html#_the_kernel_module_initialization)


[4. Authentication](https://tldp.org/LDP/www.debian.org/doc/manuals/debian-reference/ch04.en.html)


[4.1. Normal Unix authentication](https://tldp.org/LDP/www.debian.org/doc/manuals/debian-reference/ch04.en.html#_normal_unix_authentication)


[4.2. Managing account and password information](https://tldp.org/LDP/www.debian.org/doc/manuals/debian-reference/ch04.en.html#_managing_account_and_password_information)


[4.3. Good password](https://tldp.org/LDP/www.debian.org/doc/manuals/debian-reference/ch04.en.html#_good_password)


[4.4. Creating encrypted password](https://tldp.org/LDP/www.debian.org/doc/manuals/debian-reference/ch04.en.html#_creating_encrypted_password)


[4.5. PAM and NSS](https://tldp.org/LDP/www.debian.org/doc/manuals/debian-reference/ch04.en.html#_pam_and_nss)


[4.5.1. Configuration files accessed by the PAM and NSS](https://tldp.org/LDP/www.debian.org/doc/manuals/debian-reference/ch04.en.html#_configuration_files_accessed_by_the_pam_and_nss)


[4.5.2. The modern centralized system management](https://tldp.org/LDP/www.debian.org/doc/manuals/debian-reference/ch04.en.html#_the_modern_centralized_system_management)
