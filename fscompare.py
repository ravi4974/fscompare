import os,sys

def walk(path):
	return next(os.walk(path))

def sync(src,tgt):
	spath,sfolders,sfiles=walk(src)
	tpath,tfolders,tfiles=walk(tgt)

	sfolders=set(sfolders)
	tfolders=set(tfolders)

	sfiles=set(sfiles)
	tfiles=set(tfiles)

	missing_folder_tgt=sfolders.difference(tfolders)
	missing_folder_src=tfolders.difference(sfolders)

	missing_files_tgt=sfiles.difference(tfiles)
	missing_files_src=tfiles.difference(sfiles)

	output={}
	output[path]={'missing':{'target':{'folders':missing_folder_tgt,'files':missing_files_tgt},'source':{'folders':missing_folder_src,'files':missing_files_src}},'child':{}}

	common_folders=sfolders.intersect(tfolders)
	for path in common_folders:
		child_src=os.path.join(src,path)
		child_tgt=os.path.join(tgt,path)
		output['child'][path]=sync(child_src,child_tgt)

	return output

if __name__ == "__main__":
	if len(sys.argv)<3:
		print('Usage : python',os.path.basename(sys.argv[0]),'<src-path>','<target-path>')
		sys.exit(1)

	src=sys.argv[1]
	trg=sys.argv[2]

	sync(src,tgt)