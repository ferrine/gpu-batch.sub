.PHONY: readme
readme:
	@cat _readme_header.md 	> README.md
	@echo >> README.md
	@echo 'Checking Command Submission'	>> README.md
	@echo '---------------------------' >> README.md
	@echo '`--debug` flag helps to print expected submissions to LSF' >> README.md
	@echo '```' 						>> README.md
	@echo '> gpu-batch.sub --debug --batch 2 command1 command2 named:command3' >> README.md
	@./gpu-batch.sub --debug --batch 2 command1 command2 named:command3 >> README.md
	@echo '```'							>> README.md
	@echo 'command1'					> tmp.commands
	@echo 'command2'					>> tmp.commands
	@echo '<sequential> # indicates sequential jobs start'	>> tmp.commands
	@echo 'command3'					>> tmp.commands
	@echo 'command4'					>> tmp.commands
	@echo '</sequential> # indicates sequential jobs end'	>> tmp.commands
	@echo >> README.md
	@echo 'Running commands from file'	>> README.md
	@echo '--------------------------'	>> README.md
	@echo '```'							>> README.md
	@echo '> cat commands'				>> README.md
	@cat tmp.commands					>> README.md
	@echo '> gpu-batch.sub --debug -b 2 -f commands' >> README.md
	@./gpu-batch.sub --debug -b 2 -f tmp.commands >> README.md
	@echo '```' 						>> README.md
	@echo >> README.md
	@echo 'Program Description' >> README.md
	@echo '-------------------' >> README.md
	@echo '```' 						>> README.md
	@./gpu-batch.sub --help >> README.md
	@echo '```' 						>> README.md
	@pandoc --from=markdown --to=rst --output=README.rst README.md
	@rm README.md
	@rm tmp.commands

