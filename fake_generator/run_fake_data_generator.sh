#!/bin/bash

# Executa o notebook usando papermill
papermill /mnt/host/c/Users/pedro/Documents/Github/de_exp/de_exp/fake_generator/fake_data_generator.ipynb /mnt/host/c/Users/pedro/Documents/Github/de_exp/de_exp/fake_generator/fake_data_generator.ipynb

# Opcional: salvar logs
echo "Notebook executado em $(date)" >> /mnt/host/c/Users/pedro/Documents/Github/de_exp/de_exp/fake_generator/exec_logs/
