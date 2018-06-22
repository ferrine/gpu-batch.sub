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
	@echo '```' 						>> README.md
	@echo >> README.md
	@echo 'Program Description' >> README.md
	@echo '-------------------' >> README.md
	@echo '```' 						>> README.md
	@./gpu-batch.sub --help >> README.md
	@echo '```' 						>> README.md

