while getopts ":n:" opt; do
  case ${opt} in
    n )
      echo "The number picked is : $OPTARG"
      ;;
    \? )
      echo "Invalid option: -$OPTARG" >&2
      ;;
    : )
      echo "Option -$OPTARG requires an argument." >&2
      ;;
  esac
done
