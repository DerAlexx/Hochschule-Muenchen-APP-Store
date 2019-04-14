import React from "react";
import PropTypes from 'prop-types';
import AppBar from '@material-ui/core/AppBar';
import Toolbar from '@material-ui/core/Toolbar';
import { withStyles } from '@material-ui/core/styles';
import logo from './assets/logo_with_name.png';
import { FiUser, FiPlusSquare } from "react-icons/fi";

const styles = theme => ({
  root: {
    width: '100%',
  },
  grow: {
    flexGrow: 1,
  },
  menuButton: {
    marginLeft: -12,
    marginRight: 20,
  },
  title: {
    display: 'none',
    [theme.breakpoints.up('sm')]: {
      display: 'block',
    },
  },
  search: {
    position: 'relative',
    borderRadius: theme.shape.borderRadius,
    backgroundColor: '#898989',
    marginLeft: 0,
    width: '100%',
    [theme.breakpoints.up('sm')]: {
      marginLeft: theme.spacing.unit,
      width: 'auto',
    },
  },
  searchIcon: {
    width: theme.spacing.unit * 9,
    height: '100%',
    position: 'absolute',
    pointerEvents: 'none',
    display: 'flex',
    alignItems: 'center',
    justifyContent: 'center',
  },
  inputRoot: {
    color: 'inherit',
    width: '100%',
  },
  inputInput: {
    paddingTop: theme.spacing.unit,
    paddingRight: theme.spacing.unit,
    paddingBottom: theme.spacing.unit,
    paddingLeft: theme.spacing.unit * 10,
    transition: theme.transitions.create('width'),
    width: '100%',
    [theme.breakpoints.up('sm')]: {
      width: 120,
      '&:focus': {
        width: 200,
      },
    },
  },
});

function Bar(props) {
  const { classes } = props;
  return (
    <div className={classes.root}>
      <AppBar style={{position:'static'}}>
        <Toolbar style={{position:'fixed',width:'100%', backgroundColor: '#171a21', color:'#fff',  zIndex:2000}}>
        <span style={{position:'absolute', left:100, top: 8, fontSize:30, color:'#fff'}}>|</span>
        <FiPlusSquare style={{position:'absolute', left:160, top: 24, fontSize:20, color:'#fff'}} />
        <FiUser style={{position:'absolute', left:120, fontSize:20, top: 24, color:'#fff'}}/>
        <img style={{position:'absolute', right:10, width:180, height:60, zIndex:10}} src={logo} alt="Logo" />
        </Toolbar>
      </AppBar>
    </div>
  );
}

Bar.propTypes = {
  classes: PropTypes.object.isRequired,
};

export default withStyles(styles)(Bar);